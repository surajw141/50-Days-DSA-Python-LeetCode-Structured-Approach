"""Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start
and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval
newInterval = [start, end] that represents the start and end of another interval. Insert newInterval into intervals 
that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals
(merge overlapping intervals if necessary). Return intervals after the insertion. Note that you don't need to modify intervals
in-place. You can make a new array and return it. Given start values are >=0.

"""

def insert(intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)

    # Add all intervals ending before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    # Merge all overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    # Add the merged interval
    res.append(newInterval)

    # Add remaining intervals
    res.extend(intervals[i:])

    return res

# 1, 2  3,4  5,6  3,7
intervals = [[1,2],[3,4],[5,6]] 
newInterval = [3,7]
print(insert(intervals, newInterval))

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))