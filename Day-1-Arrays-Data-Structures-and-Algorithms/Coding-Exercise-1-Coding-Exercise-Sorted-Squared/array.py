"""You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.
Remember
You can solve this question in multiple ways.
Think about the following -
1.What would be the brute force way of solving this question ? What would be the Time and Space complexity of this approach?
2.Is there a better way to solve this with a more optimum Time complexity than the Brute force way ? """

# solution below
# Time = O(nlogn)  Space = O(n)
def sorted_squared(array):
    new_array = [0]*len(array)
    for i in range(len(array)):
        new_array[i] = array[i]**2
        # new_array[i] = array[i]*array[i]
    new_array.sort()
    return new_array


print(sorted_squared([-5, 1, 2]))
print(sorted_squared([0, 1, 2]))
print(sorted_squared([]))