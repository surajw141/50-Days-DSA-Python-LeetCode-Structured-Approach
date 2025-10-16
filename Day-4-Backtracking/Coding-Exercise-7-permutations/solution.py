"""#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

nums = [1,4]

Output :[[1,4],[4,1]]

Example 2:

nums = [1,4,5]

Output :[[1,4,5],[1,5,4],[4,1,5],[4,5,1],[5,1,4],[5,4,1]]"""

def permute(nums):
    n = len(nums)
    res = []
    def helper(index):
        if index == n-1:
            res.append(nums[:])
            return
        for j in range(index,n):
            nums[index],nums[j] = nums[j],nums[index]
            helper(index+1)
            nums[index],nums[j] = nums[j],nums[index]
            
    helper(0)
    return res

print(permute([1,4,5]))
print(permute([1, 4]))