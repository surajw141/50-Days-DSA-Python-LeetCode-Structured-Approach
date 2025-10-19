"""#Given an integer array nums that may contain duplicates, return all possible
subsets
(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example : 
nums = [1,3,3]
Output =
[
[],"""
def subsetsWithDup(nums):
    res = []
    nums.sort()
    def subsets(index,curr):
        if index ==len(nums):
            res.append(curr[:])
            return
        #include
        curr.append(nums[index])
        subsets(index+1,curr)
        curr.pop()
        #exclude
        while index<len(nums)-1 and nums[index]==nums[index+1]:
            index+=1
        subsets(index+1,curr)
    subsets(0,[])
    return res

#use it
print(subsetsWithDup([1,3,3]))