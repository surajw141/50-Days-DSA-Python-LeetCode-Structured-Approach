"""Question:
Two Sum - You are given an array of Integers and another integer targetValue. Write a function that will take these inputs and return the indices of the 2 integers in the array that add up targetValue.
Try:
Try to optimise your solution and arrive at a Time Complexity of O(n)
Check the Hints section to get a clue
All the best. Keep at it !"""

def two_sum(array,target):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return [i, j]
    return[]
#use it with 2 -1 5 3 ) 4
print(two_sum([2, -1, 5, 3],4))
