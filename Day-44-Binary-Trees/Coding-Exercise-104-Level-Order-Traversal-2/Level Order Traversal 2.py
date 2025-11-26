"""Coding Exercise: Level Order Traversal 2
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
(i.e., from left to right, level by level from leaf to root)."""


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_nodes)
    return result[::-1]

# Example tree:
#       3
#     /   \
#    9     20
#         /  \
#        15   7

root = TreeNode(3,
                TreeNode(9),
                TreeNode(20, TreeNode(15), TreeNode(7)))

print(levelOrderBottom(root))
