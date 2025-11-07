"""Question

Given an array, rotate the array to the right by k steps, where k is non-negative.



Try :

After you have solved this question, think about whether you can solve it in constant space"""

def rotate_array(array,k):
    if len(array) == 0:return []
    k=k%len(array)
    temp = array[-k:]
    for i in reversed(range(len(array)-k)):
        array[i+k] = array[i]
        
    for i in range(len(temp)):
        array[i] = temp[i]
        
    return array

#use it
print(rotate_array([1, 2, 3, 4, 5], 3))