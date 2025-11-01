"""Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example :

Input: nums = [1,2,-10,3,9]
Output: 12
Explanation: The subarray [3,9] has the largest sum 12."""

def maxSubArray(nums):
    #Write code here 
    max_sum = float('-inf')
    curr_sum = 0
    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

print(maxSubArray([1,2,-10,3,9]))