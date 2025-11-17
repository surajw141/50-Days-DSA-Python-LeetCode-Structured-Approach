"""Question:

Radix Sort-You are given an array of non-negative integers. Write a function that will take this array as 
and return the sorted array using Radix sort."""

def radix_sort(array):
    if len(array) == 0:
        return 'empty array'
 
    # Finding the max and the number of digits takes O(n)
    greatest_number = max(array)
    number_of_digits = len(str(greatest_number))
 
    # number of times counting sort needs to be done = digits in greatest number
    # For each digit, perform counting sort. This gives us O(d*(n+k))
    # where d is the number of digits, n is the number of elements, and k is the base (10 for decimal)
    for i in range(number_of_digits):
        counting_sort(array, i)
 
    return array
 
def counting_sort(array, place):
    output = [0] * len(array)
    temp = [0] * 10  # We're using base 10
    digit_place = 10 ** place
 
    # Counting occurrence of digits. This is O(n)
    for num in array:
        digit = (num // digit_place) % 10
        temp[digit] += 1
 
    # Calculate cumulative count. This is O(k), k is base here i.e., 10
    for i in range(1, 10):
        temp[i] += temp[i - 1]
 
    # Populate the output array. This is O(n)
    for j in range(len(array) - 1, -1, -1):
        curr_digit = (array[j] // digit_place) % 10
        temp[curr_digit] -= 1
        insert_position = temp[curr_digit]
        output[insert_position] = array[j]
 
    array[:] = output[:]
    
    
array = [3, 1, 5, 4, 2]
print(radix_sort(array))