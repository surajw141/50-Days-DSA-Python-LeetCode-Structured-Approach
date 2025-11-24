"""Coding Exercise: Construct Binary Search Tree
Question :Construct BST

Design a Binary Search Tree class that supports the following:

1.Insert a value

2.Remove a value. This method should remove the first occurrence of a value.

3.Find a value. If the value is found it should return the node with the value else return false."""



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return self

        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = node
                    return self
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    return self
                current = current.right

    def find(self, value):
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current
        return False

    def get_min_node(self, node):
        while node.left:
            node = node.left
        return node

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left = self._remove(node.left, value)

        elif value > node.value:
            node.right = self._remove(node.right, value)

        else:
            # Case 1: no children
            if not node.left and not node.right:
                return None

            # Case 2: one child
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Case 3: two children
            successor = self.get_min_node(node.right)
            node.value = successor.value
            node.right = self._remove(node.right, successor.value)

        return node


bst = BinarySearchTree()
for v in [10, 5, 15, 3, 7, 12, 17]:
    bst.insert(v)

print(bst.find(7).value)  # → 7
print(bst.find(100))      # → False

bst.remove(10)  # root remove
print(bst.root.value)     # → 12 (correct successor)


