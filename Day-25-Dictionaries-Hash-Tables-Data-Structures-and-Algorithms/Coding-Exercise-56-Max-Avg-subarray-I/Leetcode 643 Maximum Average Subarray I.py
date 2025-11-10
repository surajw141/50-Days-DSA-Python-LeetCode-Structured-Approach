"""You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.



Example:

Input: [1,13,-6,-3,40,2], k = 4

Output: 11

13 + -6 + -3 + 40 = 44; 44/4 = 11"""

def findMaxAverage(nums, k):
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(k, len(nums)):
        curr_sum = curr_sum + nums[i] - nums[i-k]
        max_sum = max(max_sum, curr_sum)
    return max_sum/k

print(findMaxAverage([1,13,-6,-3,40,2], 4))