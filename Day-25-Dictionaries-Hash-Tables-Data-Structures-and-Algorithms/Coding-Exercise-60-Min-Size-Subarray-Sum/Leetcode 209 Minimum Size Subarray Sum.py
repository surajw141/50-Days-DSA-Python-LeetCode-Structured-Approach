"""Minimum Size Subarray Sum: 
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example:
target = 15
nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
expected = 2"""

def minSubArrayLen(target, nums):
    left = 0
    currentSum = 0
    length = float('infinity')
    for right in range(len(nums)):
        currentSum += nums[right]
        while currentSum >= target:
            newLength = right - left + 1
            if newLength < length:
                length = newLength
                #print(length)
            currentSum -= nums[left]
            left += 1
                    
    return length if length != float('infinity') else 0

print(minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))