def lengthOfLIS(nums):
    n = len(nums)
    dp = [[-1]*n for _ in range(n)]
    def helper(curr,prev):
        if curr >n-1:
            return 0
        if dp[curr][prev+1]!=-1:
            return dp[curr][prev+1]

        exclude = helper(curr+1,prev)    
        include = 0    
        if prev ==-1 or nums[curr] > nums[prev]:
            include = 1 + helper(curr+1,curr)   
        dp[curr][prev+1] =  max(include,exclude)  
        return dp[curr][prev+1]   
    return helper(0,-1)

#use it
print(lengthOfLIS([300,9,2,5,3,7,500,400]))