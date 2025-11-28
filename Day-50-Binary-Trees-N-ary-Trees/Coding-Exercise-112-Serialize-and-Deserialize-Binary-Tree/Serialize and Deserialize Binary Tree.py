"""Coding Exercise: Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits 
that it can be stored in a file or memory buffer, or transmitted across a network connection link to be
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary
tree can be serialized to a string and this string can be deserialized to the original tree structure."""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class Codec:
    def serialize(self, root):
        if not root:
            return ""
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")
        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = [root]
        index = 1
        while queue:
            node = queue.pop(0)
            if values[index] != "None":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1
            if values[index] != "None":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1
            if index >= len(values):
                break
        return root

# Test tree:
#     1
#    / \
#   2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
serialized = codec.serialize(root)
print("Serialized:", serialized)

deserialized = codec.deserialize(serialized)
print("Deserialized Root:", deserialized.val)
print("Left:", deserialized.left.val)
print("Right:", deserialized.right.val)
print("Right.Left:", deserialized.right.left.val)
print("Right.Right:", deserialized.right.right.val)

