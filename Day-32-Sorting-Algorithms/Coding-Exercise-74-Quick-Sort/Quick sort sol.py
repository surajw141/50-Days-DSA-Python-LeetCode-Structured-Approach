"""Question:

Quick Sort-You are given an array of integers. Write a function that will take this array as input and return
the sorted array using Quick sort."""

# Quick Sort - Recursively QS lower sized 
# middle - pivot
#space complexity is O(log n) 
 
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]  # Space Complexity: O(1)
 
def partition(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
 
    middle = (start + end) // 2
    swap(array, start, middle)
 
    pivot = array[start]
    i = start + 1
    j = end
 
    while i <= j:
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i < j:
            swap(array, i, j)
    swap(array, start, j)
 
    # i, j, pivot, start, end take constant space
    return j
 
def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
 
    while start < end:
        pivot_idx = partition(array, start, end)
 
        # Recursively call Quick Sort on lower sized subarray
        # The maximum depth of the recursion is log(n) because we are always 
        # recursing into the smaller part of the partition. Hence, the auxiliary 
        # space used is O(log(n)) even in the worst case.
        if pivot_idx - start < end - pivot_idx:
            quick_sort(array, start, pivot_idx - 1)
            start = pivot_idx + 1
        else:
            quick_sort(array, pivot_idx + 1, end)
            end = pivot_idx - 1
            
#use function
array = [3, 1, 5, 4, 2]
quick_sort(array)
#print the output
print(array)