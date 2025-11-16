"""Question:

Selection Sort-You are given an array of integers. Write a function that will take this array as input and return the sorted array
using Selection sort."""

def selection_sort(nums):
    for i in range(len(nums)):
        smallest = i
 
        for j in range(i+1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
 
        if i != smallest:
            nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums
