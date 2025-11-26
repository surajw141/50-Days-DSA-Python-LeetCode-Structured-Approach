"""Coding Exercise: Left / Right view
Question :Left/Right View of binary tree

1. Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

2. Given the root of a binary tree, imagine yourself standing on the left side of it, 
return the values of the nodes you can see ordered from top to bottom."""


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
        #if root is None
        if self.root is None:
            if array[0] is None:
                return
            else:
                node = Node(array[0])
                self.root = node
                i += 1
                if i == len(array): 
                    return self
        #insert elements
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            #left
            if current.left is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.left = node
                i += 1
                if i == len(array): 
                    return self
            if current.left: 
                queue.append(current.left)
            #right
            if current.right is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.right = node
                i += 1
                if i == len(array): 
                    return self
            if current.right: 
                queue.append(current.right)
 
def rightView(root):
    if root is None: 
        return []
    right = []
    queue = [root]
    while queue:
        length = len(queue)
        count = 0
        while count < length:
            count += 1
            current = queue.pop(0)
            if count == length: 
                right.append(current.value)
            if current.left: 
                queue.append(current.left)
            if current.right: 
                queue.append(current.right)
    return right
 
def leftView(root):
    if root is None: 
        return []
    left = []
    queue = [root]
    while queue:
        length = len(queue)
        count = 0
        while count < length:
            count += 1
            current = queue.pop(0)
            if count == 1: 
                left.append(current.value)
            if current.left: 
                queue.append(current.left)
            if current.right: 
                queue.append(current.right)
    return left
 
tree = BinaryTree()
tree.insert([7,11,1,None,7,2,8,None,None,None,3,None,None,5,None])
print(leftView(tree.root))