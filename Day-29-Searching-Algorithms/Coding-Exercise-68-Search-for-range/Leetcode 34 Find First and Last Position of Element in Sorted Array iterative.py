def find_left_extreme(array, target):
    left = 0
    right = len(array) - 1
    while(left <= right):
        middle = (left + right) // 2
        if array[middle] == target:
            if middle == 0: return 0
            elif array[middle - 1] == target:
                right = middle - 1
            else: return middle
            
        elif target < array[middle]: right = middle - 1
        else: left = middle + 1
        
    return -1

def find_right_extreme(array, target):
    left = 0
    right = len(array) - 1
    while(left <= right):
        middle = (left + right) // 2
        if array[middle] == target:
            if middle == len(array) - 1: return middle
            elif array[middle + 1] == target:
                left = middle + 1
            else: return middle
        elif target < array[middle]: right = middle - 1
        else: left = middle + 1
    return -1

def search_for_range_iterative(array, target):
    left_extreme = find_left_extreme(array, target)
    right_extreme = find_right_extreme(array, target)
    return [left_extreme, right_extreme]

#use function
print(search_for_range_iterative([1, 1, 2, 2, 2, 3, 4], 1))
