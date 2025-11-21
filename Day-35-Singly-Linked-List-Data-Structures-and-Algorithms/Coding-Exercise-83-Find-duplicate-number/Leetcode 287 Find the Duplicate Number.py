"""Question:

Find duplicate number-Given an array of integers nums containing n + 1 integers where each integer is in the 
range [1, n] inclusive. There is only one repeated number in nums, return this repeated number. 
You must solve the problem without modifying the array nums and uses only constant extra space."""
def getDuplicate(nums):
    # Time Complexity Explanation:
    # The while loop runs at most 'n' times where 'n' is the number of elements in the array.
    # Thus, the time complexity is O(n).
    
    hare = 0
    tortoise = 0
 
    while True:
        hare = nums[nums[hare]]
        tortoise = nums[tortoise]
 
        if hare == tortoise:
            pointer = 0
            while pointer != tortoise:
                pointer = nums[pointer]
                tortoise = nums[tortoise]
            return pointer
 
# The time complexity of this function is O(n) where n is the number of elements in the array

print(getDuplicate([1, 3, 4, 2, 2]))
