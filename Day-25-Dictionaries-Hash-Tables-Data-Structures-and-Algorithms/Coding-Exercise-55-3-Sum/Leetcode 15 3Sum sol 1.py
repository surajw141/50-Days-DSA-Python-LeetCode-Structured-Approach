"""3 Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]

such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example:

Input: nums = [-2,0,2,1,-1,-3]

Output: [[-2,0,2],[0,1,-1],[2,1,-3]]



Input: nums = [-1,2,6,-1,1]

Output: [[-1,2,-1]]"""

def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i == 0 or nums[i-1] != nums[i]:
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sumThree = nums[i] + nums[left] + nums[right]
                if sumThree == 0:
                    res.append([nums[i], nums[left], nums[right]])  # Fixed line
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif sumThree < 0:
                    left += 1
                else:
                    right -= 1
    return res

# Testing the function
print(threeSum([-2, 0, 2, 1, -1, -3]))
