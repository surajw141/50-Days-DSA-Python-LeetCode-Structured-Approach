"""Coding Exercise: Unique BST 2
Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateTrees(n):
    if n == 0:
        return []
 
    def generate(start, end):
        if start > end:
            return [None]

        all_trees = []
        for i in range(start, end + 1):
            # Generate all possible left and right subtrees
            left_trees = generate(start, i - 1)
            right_trees = generate(i + 1, end)
            
            # Connect left and right subtrees to the root i
            for l in left_trees:
                for r in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = l
                    current_tree.right = r
                    all_trees.append(current_tree)
        
        return all_trees
 
    return generate(1, n)

