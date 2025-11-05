"""Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210" """
from functools import cmp_to_key

def largestNumber(nums):
    if not any(nums):
        return "0"
    
    def compare(a, b):
        return int(b + a) - int(a + b)
    
    nums = [str(num) for num in nums]
    nums.sort(key=cmp_to_key(compare))
    
    return "".join(nums)