"""Given the root of a binary tree, return the preorder traversal of its nodes' values. Write the Iterative Solution."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    res = []
    if root is None:
        return res

    stack = [root]

    while stack:
        node = stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res
