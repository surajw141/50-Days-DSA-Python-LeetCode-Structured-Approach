"""Question:

Binary Search - Given an array of integers which is sorted in ascending order, and a target integer, write a function to search for whether the target integer is there in the given array. If it is there then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.

Try:

Try to write both the iterative and recursive solution.

Keep at it !"""

def binary_search_iterative(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
            
        else:
            right = middle - 1
            
    return -1

#print ( 2, 3 7 9 11 23 37 81 87 89) 87 )
print(binary_search_iterative([2, 3, 7, 9, 11, 23, 37, 81, 87, 89], 87))
