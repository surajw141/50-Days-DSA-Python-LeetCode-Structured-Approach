def twoCitySchedCost(costs):
    def minCost(i, a_count):
        # Base case: when all people have been considered
        if i == len(costs):
            # Base case: if we've considered all people, we wil have sent exactly n to A. 
            #so we can just return 0. There is no need to again check whether n people 
            #are sent to city A
            return 0
 
        # Cost of sending the i-th person to City A
        if a_count < len(costs) // 2:
            costA = costs[i][0] + minCost(i + 1, a_count + 1)
        else:
            costA = float('inf')  # Prevent sending more than n people to City A
        
        # Cost of sending the i-th person to City B
        b_count = i - a_count  # Number of people sent to City B so far
        if b_count < len(costs) // 2:
            costB = costs[i][1] + minCost(i + 1, a_count)
        else:
            costB = float('inf')  # Prevent sending more than n people to City B
 
        # Return the minimum cost of the two choices
        return min(costA, costB)
 
    # Start the recursion from the 0-th index with 0 people sent to A
    return minCost(0, 0)

#use it
print(twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))