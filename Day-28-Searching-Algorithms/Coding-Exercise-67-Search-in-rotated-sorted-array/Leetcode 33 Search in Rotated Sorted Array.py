"""Question:

Search in Rotated Sorted array- You are given an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such 
that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).  
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. Given an integer target,
return the index of target if it is in the array, else return -1. You must write an algorithm with O(log n) runtime complexity."""

def search_rotated_sorted_array(nums,target):
    left = 0
    right = len(nums) - 1
    while (left <= right):
        middle = (left + right) // 2
        if nums[middle] == target:return middle
        if nums[left] <= nums[middle]:
            if target >= nums[left] and target < nums[middle]:
                right = middle - 1
                # print("left")
            else:
                left = middle + 1
        else:
            if target <= nums[right] and target > nums[middle]:
                left = middle + 1
                # print("right")
            else:
                right = middle - 1
                # print("right")
    return -1

# print (7 8 1 2 3 4 5 6 ) 3
print(search_rotated_sorted_array([7, 8, 1, 2, 3, 4, 5, 6], 3))