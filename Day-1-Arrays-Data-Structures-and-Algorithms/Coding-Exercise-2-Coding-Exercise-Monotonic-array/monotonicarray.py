def monotonic_array(array):
    
    n = len(array)
    if n == 0: return True
    first = array[0]
    last = array[n-1]
    if first >last:
        #MD or array is not monotonic
        for k in range(n-1):
            if array[k] < array[k+1]: return False
    
    elif first == last:
        #M - all values are equal
        for ke in range(n-1):
            if array[ke] != array[ke+1]: return False
    else:
        #first < last
        #MI or not M
        for k in range(n-1):
            if array[k] > array[k+1]: return False
    return True

print(monotonic_array([1, 1, 1, 1, 1, 1, 1, 1]))
print(monotonic_array([1, 2, 3, 4, 5, 6, 7, 8]))
print(monotonic_array([8, 7, 6, 5, 4, 3, 2, 1]))