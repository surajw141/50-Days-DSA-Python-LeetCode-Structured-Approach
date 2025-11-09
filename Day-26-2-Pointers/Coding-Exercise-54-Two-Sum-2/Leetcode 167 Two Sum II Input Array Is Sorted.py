"""Two Sum II

Given a 1-indexed array of integer numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers, index1 and index2, array [index1, index2] of length 2.

It is guaranteed that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.



Example: Input: numbers = [1,3,4], target = 5; Output: [1,3]"""

def twoSum(numbers, target):
    left = 0
    right = len(numbers)-1
    while left < right:
        currentSum = numbers[left] + numbers[right]
        if currentSum == target:
            return [left+1, right+1]
        elif currentSum < target:
            left += 1
        else:
            right -= 1
            
print(twoSum([1,3,4], 5))