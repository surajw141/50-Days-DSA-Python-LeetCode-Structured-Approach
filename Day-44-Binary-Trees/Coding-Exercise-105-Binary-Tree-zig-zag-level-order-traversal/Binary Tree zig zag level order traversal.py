"""Coding Exercise: Binary Tree zig zag level order traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between)."""

from collections import deque
 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
 
def zigzagLevelOrder(root):
    if not root:
        return []
    
    # Initialize the queue with the root node and a variable to keep track of the current level's direction
    queue = deque([root])
    result = []
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level_nodes = deque()  # Use deque to efficiently append on both ends
        
        # Process each node in the current level
        for _ in range(level_size):
            node = queue.popleft()
            if left_to_right:
                level_nodes.append(node.val)  # Append to the right for left-to-right
            else:
                level_nodes.appendleft(node.val)  # Append to the left for right-to-left
            
            # Add child nodes to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(list(level_nodes))  # Convert deque to list and add to the result
        left_to_right = not left_to_right  # Toggle the direction for the next level
    
    return result

# Build the example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Test
print(zigzagLevelOrder(root))
