"""Coding Exercise: N-ary Tree Level Order Traversal
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples)."""

from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        if children is None:
            self.children = []
        else:
            self.children = children

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            for child in node.children:
                queue.append(child)
        result.append(current_level)
    
    return result

# Example usage with a sample N-ary tree
root = Node(1, [
    Node(3, [Node(5), Node(6)]),
    Node(2),
    Node(4)
])

# Run levelOrder function
print(levelOrder(root))


