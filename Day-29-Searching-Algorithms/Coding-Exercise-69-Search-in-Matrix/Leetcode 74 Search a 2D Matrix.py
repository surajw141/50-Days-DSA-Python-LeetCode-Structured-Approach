"""Question:

Search in 2D Array-Write an efficient algorithm that searches for a value target in an m x n integer matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
If the value is there in the matrix return true, else false.



Try :

Try to write the solution with T=O(mn) where m and n are the number of rows and number of columns respectively."""

def search_in_matrix(matrix,target):
    column = len(matrix[0])
    rows = len(matrix)
    top = 0
    bottom = rows - 1
    while(top <= bottom):
        middle = (top + bottom) // 2
        if target < matrix[middle][0]: bottom = middle - 1
        elif target > matrix[middle][column - 1]: top = middle + 1
        else: break
    if top > bottom: return False
    
    if top > bottom: return False
    left = 0
    right = column - 1
    
    while(left <= right):
        middle = (left + right) // 2
        if target == matrix[middle][middle]: return True
        elif target < matrix[middle][middle]: right = middle - 1

    return False

matrix = [[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12], [20, 30, 40, 50]]

print(search_in_matrix(matrix, 45))