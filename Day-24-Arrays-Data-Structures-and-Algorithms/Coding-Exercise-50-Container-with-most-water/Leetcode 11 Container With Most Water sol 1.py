"""Question
Container with most Water - You are given an integer array height of length n. There are n vertical lines drawn such 
the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a
container, such that the container contains the most water(depth is constant across containers). Return the area(that
the 2 lines and the X axis make) of container which can store the max amount of water. Notice that you may not slant
the container.
Try
To optimise your solution . In case you approached this question with the Brute force method your Time Complexity 
might be O(n^2).
Try to write a better solution with Time Complexity O(n)"""

def max_area(array):
    max_area = 0
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            area = min(array[i], array[j]) * (j-i)
            max_area = max(max_area, area)
            
    return max_area

#use it with 3 7 5 6 8 4
print(max_area([3, 7, 5, 6, 8, 4]))
