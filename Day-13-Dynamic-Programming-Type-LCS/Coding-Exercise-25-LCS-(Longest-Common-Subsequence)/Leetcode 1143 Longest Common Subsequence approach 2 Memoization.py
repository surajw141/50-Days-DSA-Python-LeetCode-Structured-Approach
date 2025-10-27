def longestCommonSubsequence(text1, text2):
    n = len(text1)
    m = len(text2)
    dp = [[-1]*m for _ in range(n)]
    def helper(index1,index2):
        #base case
        if index1>n-1 or index2>m-1:
            return 0

        if dp[index1][index2]!=-1:
            return dp[index1][index2]    

        #recursive case
        if text1[index1]==text2[index2]:
            dp[index1][index2]=1+ helper(index1+1,index2+1)
            return dp[index1][index2]
        dp[index1][index2]=max(helper(index1+1,index2), helper(index1,index2+1)) 
        return dp[index1][index2]   
    return helper(0,0)    

print(longestCommonSubsequence("pbcdq", "pcq"))