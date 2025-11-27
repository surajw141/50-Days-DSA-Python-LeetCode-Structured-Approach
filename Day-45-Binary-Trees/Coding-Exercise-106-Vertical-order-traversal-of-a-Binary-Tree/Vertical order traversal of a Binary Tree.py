"""Coding Exercise: Vertical order traversal of a Binary Tree
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
from collections import deque, defaultdict
 
def verticalTraversal(root):
    if not root:
        return []
    
    # Store the nodes along with their positions
    node_list = []
    
    # Queue for BFS: stores node along with its row and column index
    queue = deque([(root, 0, 0)])
    
    while queue:
        node, row, col = queue.popleft()
        if node:
            node_list.append((col, row, node.val))
            queue.append((node.left, row + 1, col - 1))
            queue.append((node.right, row + 1, col + 1))
    
    # Sort the node list by column, row, then value
    node_list.sort()
    
    # Group by column index and extract values
    res = defaultdict(list)
    for col, _, val in node_list:
        res[col].append(val)
    
    # Return sorted columns
    return [res[col] for col in sorted(res)]

