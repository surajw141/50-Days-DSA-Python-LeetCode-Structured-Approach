"""You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: nums = [4, 1, 1, 3, 1, 1, 1]
Output: 2
Explanation:
The minimum number of jumps to reach the last index (6) is 2:
Jump from index 0 to index 4.
Jump from index 4 to index 6."""

def jump(nums):
    if len(nums) == 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(len(nums) - 1):  # we don’t need to process the last index
        farthest = max(farthest, i + nums[i])
        # if we have come to the end of the range of the current jump
        if i == current_end:
            jumps += 1
            current_end = farthest
            # early exit if we can already reach the end
            if current_end >= len(nums) - 1:
                break
    return jumps
print(jump([2, 3, 1, 1, 4]))
print(jump([4, 1, 1, 3, 1, 1, 1]))