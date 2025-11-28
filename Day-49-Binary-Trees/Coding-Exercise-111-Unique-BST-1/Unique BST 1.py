"""Coding Exercise: Unique BST 1
Given an integer n, return the number of structurally unique BST's (binary search trees) which has 
exactly n nodes of unique values from 1 to n."""

def numTrees(n):
    dp = [0] * (n+1)
    dp[0] = 1  # Base case for an empty tree
    if n >= 1:
        dp[1] = 1  # There is only one BST with one node
    
    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1] * dp[i-j]
            
    return dp[n]
# Test the function with an example
n = 3
print("Number of unique BSTs with", n, "nodes is:", numTrees(n))
