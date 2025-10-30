"""Palindrom Partitioning 2 : 



Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:

Input: s = "ppq"
Output: 1
Explanation: The palindrome partitioning ["pp","q"] could be produced using 1 cut."""

#backtracking ( without dynamic programming)
def minCut(s):
    def isPalindrome(start,end):
        while start<end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True
    def partitions(start,end):
        #base case
        if start ==end or isPalindrome(start,end):
            return 0
        minimumCuts = end - start    
        for endIndex in range(start,end):
            if isPalindrome(start,endIndex):
                minimumCuts = min(minimumCuts,1+partitions(endIndex+1,end))
        return minimumCuts    
    return partitions(0,len(s)-1)    

#use it
print(minCut("ppq"))