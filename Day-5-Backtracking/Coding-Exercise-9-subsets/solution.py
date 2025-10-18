#Power Set - Given an integer array of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

def power_set (nums):
    output = []
    def helper (nums,i,subset):
        if i == len(nums):
            output.append(subset.copy())
            return
        helper(nums,i+1,subset)
        subset.append(nums[i])
        helper(nums,i+1,subset)
        subset.pop()
    helper(nums,0,[])
    return output

# use it 
print(power_set([1,2,3]))
print(power_set([1, 2, 3, 4]))
