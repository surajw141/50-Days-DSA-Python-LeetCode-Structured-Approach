"""Coding Exercise: Construct Binary Tree from Pre order and In order Traversal
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, construct and return the binary tree."""

# ---------------------------------------------------------
# Definition for a binary tree node
# ---------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ---------------------------------------------------------
# Build Tree from Preorder + Inorder
# ---------------------------------------------------------
def buildTree(preorder, inorder):
    def constructBinaryTree(pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end or in_start > in_end:
            return None

        # Root is always the first element in preorder
        root = TreeNode(preorder[pre_start])

        # Index of root in inorder array
        index_in = index_map[root.val]

        # Number of nodes in left subtree
        left_count = index_in - in_start

        # Recursively build left and right subtrees
        root.left = constructBinaryTree(
            pre_start + 1,
            pre_start + left_count,
            in_start,
            index_in - 1
        )

        root.right = constructBinaryTree(
            pre_start + left_count + 1,
            pre_end,
            index_in + 1,
            in_end
        )

        return root

    # Precompute positions of elements in inorder traversal
    index_map = {value: i for i, value in enumerate(inorder)}

    return constructBinaryTree(0, len(preorder) - 1, 0, len(inorder) - 1)


# ---------------------------------------------------------
# Traversal functions to verify the constructed tree
# ---------------------------------------------------------
def print_inorder(node):
    if not node:
        return
    print_inorder(node.left)
    print(node.val, end=" ")
    print_inorder(node.right)

def print_preorder(node):
    if not node:
        return
    print(node.val, end=" ")
    print_preorder(node.left)
    print_preorder(node.right)


# ---------------------------------------------------------
# Example Usage
# ---------------------------------------------------------
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = buildTree(preorder, inorder)

print("Inorder Traversal of built tree:")
print_inorder(root)   # Expected: 9 3 15 20 7

print("\nPreorder Traversal of built tree:")
print_preorder(root)  # Expected: 3 9 20 15 7
