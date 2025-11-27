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
        if self.root is None:
            if array[0] is None: 
                return
            else:
                node = Node(array[0])
                self.root = node
                i += 1
                if i == len(array): 
                    return self
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.left = node
                i += 1
                if i == len(array): 
                    return self
            if current.left is not None: 
                queue.append(current.left)
            if current.right is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.right = node
                i += 1
                if i == len(array): 
                    return self
            if current.right is not None: 
                queue.append(current.right)
 
def invertRecursive(node):
    if node is None: 
        return
 
    temp = node.left
    node.left = node.right
    node.right = temp
 
    invertRecursive(node.left)
    invertRecursive(node.right)
    return node
 
tree = BinaryTree()
tree.insert([1,2,3,4,None,None,5,6,None,7])
 
invertRecursive(tree.root)