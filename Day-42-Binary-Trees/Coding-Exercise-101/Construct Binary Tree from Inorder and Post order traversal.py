"""Coding Exercise: Construct Binary Tree from Inorder and Post order traversal
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree 
and postorder is the postorder traversal of the same tree, construct and return the binary tree."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def buildTree(inorder, postorder):
    def constructBinaryTree(post_start,post_end,in_start,in_end):
        #base case
        if post_start>post_end or in_start>in_end:
            return None
 
        #recursive case
        root = TreeNode(postorder[post_end])
        index_root = hash[root.val]
        number_of_elements_right = in_end-index_root
        root.left=constructBinaryTree(post_start,post_end-number_of_elements_right-1,in_start,index_root-1)
        root.right=constructBinaryTree(post_end-number_of_elements_right,post_end-1,index_root+1,in_end)
        return root
 
    n= len(inorder)
    hash={}
    for i in range(n):
        hash[inorder[i]]=i
    return constructBinaryTree(0,n-1,0,n-1) 



# Test example
inorder = [2, 1, 4, 3, 5]
postorder = [2, 4, 5, 3, 1]

root = buildTree(inorder, postorder)

# Function to print tree in preorder to verify
def print_preorder(node):
    if not node:
        return
    print(node.val, end=" ")
    print_preorder(node.left)
    print_preorder(node.right)

print("Preorder traversal of constructed tree:")
print_preorder(root)
