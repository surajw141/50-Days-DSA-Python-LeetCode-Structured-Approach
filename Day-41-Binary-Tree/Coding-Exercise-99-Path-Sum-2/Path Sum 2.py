r"""Path Sum 2
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.



Example



# Corrected Tree structure:
    #     5
    #    / \
    #   4   8
    #  /   / \
    # 11  13  4
    # / \    / \
    #7   2  5   1
        
Output = [[5, 4, 11, 2], [5, 8, 4, 5]] 
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def pathSum(root, targetSum):
    #write code here
    res = []
    
    def helper(node, curr, rem_sum):
        if node is None: return
        
        #recursive case
        curr.append(node.val)
        if rem_sum == node.val and node.right is None and node.left is None:
            res.append(list(curr[:]))
            
        else:
            helper(node.left, curr, rem_sum - node.val)
            helper(node.right, curr, rem_sum - node.val)
        curr.pop()
    helper(root, [], targetSum)
    return res

# Example usage:
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

targetSum = 22
print(pathSum(root, targetSum))  
# Expected output: [[5, 4, 11, 2], [5, 8, 4, 5]]
