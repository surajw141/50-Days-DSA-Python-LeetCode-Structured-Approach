"""Given an integer array nums, find a subarray that has the largest product, and return the product.



Example :

Input: nums = [3,3,-2,4]
Output: 9
Explanation: [3,3] has the largest product 9."""

"""Your code failed this test
Error details
2 != 6 : Should be 6"""

def maxProduct(nums):
    #Write code here 
    max_product = nums[0]
    curr_max = nums[0]
    curr_min = nums[0]
    for i in range(1, len(nums)):
        temp = curr_max
        curr_max = max(nums[i], nums[i]*curr_max, nums[i]*curr_min)
        curr_min = min(nums[i], nums[i]*temp, nums[i]*curr_min)
        max_product = max(max_product, curr_max)
    return max_product

print(maxProduct([3,3,-2,4]))