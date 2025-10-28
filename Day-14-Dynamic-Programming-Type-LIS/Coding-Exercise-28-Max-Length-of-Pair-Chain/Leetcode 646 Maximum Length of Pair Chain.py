"""You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.



Example 1:

Input: pairs = [[2,3],[3,4],[4,5]]
Output: 2
Explanation: The longest chain is [2,3] -> [4,5]."""

def findLongestChain(pairs):
    n = len(pairs)
    pairs.sort()
    dp = [1]*n
    res = 1
    for i in range(1,n):
        for j in range(i):
            if pairs[j][1] < pairs[i][0] and dp[j]+1>dp[i]:
                dp[i]=dp[j]+1
        if dp[i]>res: res = dp[i]
    return res

print(findLongestChain([[2,3],[3,4],[4,5]]))