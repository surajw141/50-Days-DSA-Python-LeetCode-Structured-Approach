"""Question:

Merge Sort-You are given an array of integers. Write a function that will take this array as input and return the
sorted array using Merge sort."""

def merge_sorted_arrays(array1, array2):
    merged_array = []
    i, j = 0, 0
 
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1
    
    while i < len(array1):
        merged_array.append(array1[i])
        i += 1
    while j < len(array2):
        merged_array.append(array2[j]);
        j += 1
 
    return merged_array
 
def merge_sort(array):
    if len(array) <= 1:
        return array
    
    middle = len(array) // 2
 
    left_side = merge_sort(array[:middle])
    right_side = merge_sort(array[middle:])
 
    return merge_sorted_arrays(left_side, right_side)

print(merge_sort([3, 1, 5, 4, 2]))