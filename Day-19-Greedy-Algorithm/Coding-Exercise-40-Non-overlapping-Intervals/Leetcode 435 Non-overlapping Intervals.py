"""Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example:

[[1, 4], [2, 5], [5, 6], [3, 4]]

Output: In this example, removing [2, 5] and [3, 4] is sufficient. Thus, the answer is 2."""

""" when empty intervals: Error shown details
list index out of range"""

def eraseOverlapIntervals(intervals):
    if not intervals:  # handle empty input
        return 0
    
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    count = 1
    end = intervals[0][1]
    
    for i in range(1, n):
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]
            
    return n - count


# Test cases
print(eraseOverlapIntervals([[1, 4], [2, 5], [5, 6], [3, 4]]))  # ✅ should return 2
print(eraseOverlapIntervals([]))  # ✅ should return 0
