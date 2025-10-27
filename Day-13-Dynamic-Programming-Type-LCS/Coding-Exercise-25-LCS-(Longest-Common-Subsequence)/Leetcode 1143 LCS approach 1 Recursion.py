#Leetcode-1143-Longest-Common-Subsequence-approach-1-Recursion
"""Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

•For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example: 

Input: text1 = "pbcdq", text2 = "pcq" 
Output: 3  
Explanation: The longest common subsequence is "pcq" and its length is 3."""
def longestCommonSubsequence(text1, text2):
    n = len(text1)
    m = len(text2)
    def helper(index1,index2):
        #base case
        if index1>n-1 or index2>m-1:
            return 0

        #recursive case
        if text1[index1]==text2[index2]:
            return 1+ helper(index1+1,index2+1)
        return max(helper(index1+1,index2), helper(index1,index2+1))    
    return helper(0,0)

#use it
print(longestCommonSubsequence("pbcdq", "pcq"))