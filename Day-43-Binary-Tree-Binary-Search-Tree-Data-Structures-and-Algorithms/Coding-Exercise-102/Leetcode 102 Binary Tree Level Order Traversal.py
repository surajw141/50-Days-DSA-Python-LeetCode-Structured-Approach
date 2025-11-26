"""Coding Exercise: Instance method, Level Order traversal
Question 1:Level Order traversal

Write a function that takes the root of a binary tree, and returns the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

1- Initially write an instance method for the Binary Search tree class to insert the values given as an array into 
the Binary tree (from left to right, level by level). Each value in the array which is not null is to be made a node
and added to the tree. (See examples in the question video).
2- Then write the function mentioned first."""

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, array):
        if len(array) == 0:
            return
        
        i = 0

        # If root is null
        if self.root is None:
            if array[0] is None:
                return
            else:
                node = Node(array[0])
                self.root = node
                i += 1
                if i == len(array):
                    return self

        # Insert elements
        queue = [self.root]
        while queue:
            current = queue.pop(0)

            # Process left child
            if current.left is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.left = node
                i += 1
                if i == len(array):
                    return self
            if current.left is not None:
                queue.append(current.left)

            # Process right child
            if current.right is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.right = node
                i += 1
                if i == len(array):
                    return self
            if current.right is not None:
                queue.append(current.right)

# Level Order Traversal function
def level_order_traversal(root):
    if root is None:
        return []
    
    output = []
    queue = deque([root])
    while queue:
        length = len(queue)
        curr_level_values = []
        for _ in range(length):
            curr = queue.popleft()
            curr_level_values.append(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        output.append(curr_level_values)
    
    return output

# Test the function with an example
tree = BinaryTree()
tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])

# Perform level order traversal
level_order = level_order_traversal(tree.root)
print(level_order)
