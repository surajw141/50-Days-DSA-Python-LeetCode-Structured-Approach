"""Post Order Traversal of Binary Tree - Iterative
Given the root of a binary tree, return the postorder traversal of its nodes' values. Write the iterative solution."""

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def postorderTraversal(root):
    stack = [root]
    res = []
    visited = [False]
    while stack:
        curr = stack.pop()
        visit = visited.pop()
        if curr:
            if visit:
                res.append(curr.val)
            else:
                stack.append(curr)
                visited.append(True)
                stack.append(curr.right)
                visited.append(False)
                stack.append(curr.left)
                visited.append(False)
    return res

# Example usage:
root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
print(postorderTraversal(root))  # Expected output: [3, 2, 1]