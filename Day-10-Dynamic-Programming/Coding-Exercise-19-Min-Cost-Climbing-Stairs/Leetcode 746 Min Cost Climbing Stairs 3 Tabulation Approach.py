"""You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,20,30]
Output: 20
Explanation: You will start at index 1.
- Pay 20 and climb two steps"""

def minCostClimbingStairs(cost):
    #tabulation, Bottom up
    n = len(cost)
    #each element in the array will be the cost of reaching that index, not cost of using 
    arr = [-1]*(n+1)
    #as you can start at step with index 0 or 1
    arr[0]=0
    arr[1]=0
    for i in range(2,n+1):
        prevOne = cost[i-1]+ arr[i-1]
        prevTwo = cost[i-2]+arr[i-2]
        arr[i] = min(prevOne,prevTwo)
    return arr[n]    

#use it
print(minCostClimbingStairs([10,20,30]))