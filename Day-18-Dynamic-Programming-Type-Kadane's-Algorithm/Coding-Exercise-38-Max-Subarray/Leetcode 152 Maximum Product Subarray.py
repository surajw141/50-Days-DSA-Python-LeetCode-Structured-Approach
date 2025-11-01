"""Given an integer array nums, find a subarray that has the largest product, and return the product.



Example :

Input: nums = [3,3,-2,4]
Output: 9
Explanation: [3,3] has the largest product 9."""

def maxProductSubarray(nums):
    #Write code here 
    max_product = float('-inf')
    curr_product = 1
    for num in nums:
        curr_product = max(num, curr_product * num)
        max_product = max(max_product, curr_product)
    return max_product

print(maxProductSubarray([3,3,-2,4]))