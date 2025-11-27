""""""

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
        # if root is null
        if self.root is None:
            if array[0] is None:
                return
            else:
                node = Node(array[0])
                self.root = node
                i += 1
                if i == len(array):
                    return self
        # insert elements
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            # left
            if current.left is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.left = node
                i += 1
                if i == len(array):
                    return self
            if current.left is not None:
                queue.append(current.left)
            # right
            if current.right is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.right = node
                i += 1
                if i == len(array):
                    return self
            if current.right is not None:
                queue.append(current.right)
 
def invertIterative(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        temp = current.right
        current.right = current.left
        current.left = temp
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return root
 
 
tree = BinaryTree()
tree.insert([1,2,3,4,None,None,5,6,None,7])
 
invertIterative(tree.root)

def printLevelOrder(root):
    if root is None:
        print("Empty")
        return
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    print(result)



from collections import deque

# --- your classes here ----

tree = BinaryTree()
tree.insert([1,2,3,4,None,None,5,6,None,7])

print("Before invert:")
printLevelOrder(tree.root)

invertIterative(tree.root)

print("After invert:")
printLevelOrder(tree.root)
