"""You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,20,30]
Output: 20
Explanation: You will start at index 1.
- Pay 20 and climb two steps"""

def minCostClimbingStairs(cost):
    n = len(cost)
    #helper(index) will return the min cost of reaching the top starting at index which 
    #means using the step at index
    array = [-1]*n
    def helper(index):
        if index >=n :return 0
        if array[index]!=-1:
            return array[index]
        #climb one
        one = cost[index] + helper(index+1)
        #climb two
        two = cost[index]+ helper(index+2)
        array[index]=min(one,two)
        return array[index]

    return min(helper(0),helper(1))    


#use it
print(minCostClimbingStairs([10,20,30]))