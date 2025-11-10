#Leetcode 1838 Frequency of the Most Frequent Element
"""The frequency of an element is the number of times it occurs in an array.
You are given an integer array nums and an integer k. In one operation, you can choose an 
index of nums and increment the element at that index by 1.
Return the maximum possible frequency of an element after performing at most k operations.

Example:
Input: nums = [2,3,5], k = 5
Output: 3"""

def maxFrequency(nums, k):
    nums.sort()
    left = 0
    total = 0
    res = 0
    for right in range(len(nums)):
        total += nums[right]
        while nums[right]*(right-left+1) > total+k:
            total -= nums[left]
            left += 1
        res = max(res, right-left+1)
    return res