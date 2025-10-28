"""Given an integer array nums, return the length of the longest strictly increasing

subsequence.



Example 1:

Input: nums = [300,9,2,5,3,7,500,400]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,500], 
therefore the length is 4."""

def lengthOfLIS(nums):
    n = len(nums)
    def helper(curr,prev):
        if curr >n-1:
            return 0
        exclude = helper(curr+1,prev)    
        include = 0    
        if prev ==-1 or nums[curr] > nums[prev]:
            include = 1 + helper(curr+1,curr)   
        return max(include,exclude)     
    return helper(0,-1)    

print(lengthOfLIS([300,9,2,5,3,7,500,400]))