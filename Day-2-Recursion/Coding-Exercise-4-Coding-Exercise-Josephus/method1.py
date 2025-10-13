def findTheWinner(n, k):
    
    #creating n = 4, arr=[1,2,3,4]
    arr = [i+1 for i in range(n)]
    #1,2,3,4
    #0,1,2,3
    def helper(arr, start_index):
        #base case
        if len(arr) == 1:
            return arr[0]
        #recursive case
        index_to_remove = (start_index + k - 1) % len(arr)
        del arr[index_to_remove]
        return helper(arr, index_to_remove)
    return helper(arr, 0)
print(findTheWinner(6, 5))