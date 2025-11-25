"""Inorder Traversal with stack
Given the root of a binary tree, return the inorder traversal of its nodes' values. Write the Iterative Solution.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    #write code here
    res = []
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

root = TreeNode(1)
root.right = TreeNode(2, TreeNode(3))

print(inorderTraversal(root))  # Expected output: [1, 3, 2]