"""Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example:

Input: intervals = [[2,3],[3,4],[2,4]]

Output: 1

Need to remove [2,4]"""

def eraseOverlapIntervals(intervals):
    intervals.sort()
    count = 0
    last = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < last:
            count += 1
            last = min(last, intervals[i][1])
            
        else:
            last = intervals[i][1]
    return count

print(eraseOverlapIntervals([[2,3],[3,4],[2,4]]))
