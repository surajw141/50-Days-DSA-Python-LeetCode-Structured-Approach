def twoCitySchedCost(costs):
    n = len(costs) // 2
    memo = {}
 
    def minCost(i, a_count):
        if i == len(costs):
            # Base case: if we've considered all people, we wil have sent exactly n to A. 
            #so we can just return 0. There is no need to again check whether n people 
            #are sent to city A
            return 0 
        if (i, a_count) in memo:
            return memo[(i, a_count)]
        
        # Cost of sending the i-th person to A
        costA = costs[i][0] + minCost(i + 1, a_count + 1) if a_count < n else float('inf')
        # Cost of sending the i-th person to B
        costB = costs[i][1] + minCost(i + 1, a_count) if (i - a_count) < n else float('inf')
        
        # Store the result in memo dictionary and return the minimum cost
        memo[(i, a_count)] = min(costA, costB)
        return memo[(i, a_count)]
 
    # Start the recursion from the 0-th index with 0 people sent to A
    return minCost(0, 0)

# use it
print(twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))