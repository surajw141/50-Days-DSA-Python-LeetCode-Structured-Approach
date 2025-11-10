def threesum(nums):
    res = set()
    for i in range(len(nums)):
        need = set()
        for j in range(i+1, len(nums)):
            valueNeeded = -(nums[i]+nums[j])
            if valueNeeded in need:
                triplet = tuple(sorted([nums[i], nums[j], valueNeeded]))
                res.add(triplet)
                
            need.add(nums[j])
    return [list(triplet) for triplet in res]

# test the function
print(threesum([-2, 0, 2, 1, -1, -3]))