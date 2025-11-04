"""A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city."""

def twoCitySchedCost(costs):
    costs.sort(key=lambda x: x[0] - x[1])
    cost = 0
    n = len(costs)
    for i in range(n//2):
        cost += costs[i][0]
        
    for i in range(n//2, n):
        cost += costs[i][1]
        
    return cost

#use it
print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))