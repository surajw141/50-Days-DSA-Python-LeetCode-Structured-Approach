"""Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.


Example:

Input: nums = [2,3,-2,-4,5,2,8,11], k = 3

Output: [3,3,5,5,8,11]"""

from collections import deque
def maxSlidingWindow(nums, k):
    dq = deque()
    output = []
    for i in range(k):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
    output.append(nums[dq[0]])
    
    for i in range(k, len(nums)):
        if dq and dq[0] == i-k:
            dq.popleft()
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        output.append(nums[dq[0]])
    
    return output

print(maxSlidingWindow([2,3,-2,-4,5,2,8,11], 3))