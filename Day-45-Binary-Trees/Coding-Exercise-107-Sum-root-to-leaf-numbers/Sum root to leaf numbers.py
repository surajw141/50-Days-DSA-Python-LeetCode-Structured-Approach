"""Coding Exercise: Sum root to leaf numbers
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def sumNumbers(root):
    def helper(node,sofar_sum):
        #base case
        if node == None:
            return 0
        if node.left == None and node.right == None:
            return sofar_sum*10 + node.val
        #recursive case
        return helper(node.left,sofar_sum*10+node.val) + helper(node.right,sofar_sum*10+node.val)
 
    return helper(root,0)

