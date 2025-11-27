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
        if self.root is None:
            if array[0] is None:
                return
            else:
                node = Node(array[0])
                self.root = node
                i += 1
                if i == len(array):
                    return self
 
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
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
 
def diameterBinaryTree(root):
    if not root:
        return 0
    maxDiameter = 0
    def dfs(node):
        nonlocal maxDiameter
        if not node:
            return -1
        leftHeight = dfs(node.left)
        rightHeight = dfs(node.right)
        diameter = leftHeight + rightHeight + 2
        maxDiameter = max(maxDiameter, diameter)
        return max(leftHeight, rightHeight) + 1
    dfs(root)
    return maxDiameter
 
tree = BinaryTree()
tree.insert([1, 3, 2, 7, 4, None, None, 8, None, None, 5, 9, None, None, 6])
print(diameterBinaryTree(tree.root))

